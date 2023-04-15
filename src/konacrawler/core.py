import abc
from typing import Optional, Type, TypedDict
import sys
from collections import defaultdict
import importlib
from pathlib import Path
import logging
from itertools import chain

__all__ = ['ModuleInfo','KNCRModule','register_module']

class ModuleInfo(TypedDict):
    name:str
    scope:list[str]


class KNCRModule(abc.ABC):
    # @property
    @staticmethod
    def info()->ModuleInfo:
        ...
        
    def crawl(self,url:str)->str:
        ...

class Registry:
    def __init__(self) -> None:
        self._module_to_models = defaultdict(set)  # dict of sets to check membership of model in module
        self._model_to_module = {}  # mapping of model names to module names
        self._model_entrypoints = {}  # mapping of model names to entrypoint fns
        self._hosts_to_models = {}

    
    @property
    def module_to_models(self):
        return self._module_to_models
    
    @property
    def hosts_to_models(self):
        return self._hosts_to_models

    @property
    def model_entrypoints(self):
        return self._model_entrypoints

    
    def register_module(self,fn):
        # lookup containing module
        mod = sys.modules[fn.__module__]
        module_name_split = fn.__module__.split('.')
        module_name = module_name_split[-1] if len(module_name_split) else ''

        # add model to __all__ in module
        model_name = fn.__name__
        if hasattr(mod, '__all__'):
            mod.__all__.append(model_name)
        else:
            mod.__all__ = [model_name]

        # add entries to registry dict/sets
        self._model_entrypoints[model_name] = fn
        self._model_to_module[model_name] = module_name
        self._module_to_models[module_name].add(model_name)
        for i in fn.info()["scope"]:
            self._hosts_to_models[i]=fn

        return fn

registry=Registry()
register_module=registry.register_module

def import_modules(custom_module=None):
    modules_path = Path(__file__).parent/'modules'
    if not modules_path.exists() or not modules_path.is_dir():
        raise ImportError("No modules folder")
    sys.path.insert(0, str(modules_path.absolute()))
    it=modules_path.glob("*")
    if custom_module:
        custom_module=Path(custom_module)
        it=chain(it,custom_module.glob("*"))
        sys.path.insert(0, str(custom_module.absolute()))
    
    # ensure that user modules are only imported once
    import_modules.memo = getattr(import_modules, "memo", set())
    for module_pth in it:
        if not module_pth.is_dir() and module_pth.suffix != ".zip" and module_pth.suffix != ".py":
            logging.warn(f"Skip {module_pth} to load")
            continue

        module_name = module_pth.stem
        module_parent = module_pth.parent.absolute()
        if module_name not in import_modules.memo:
            import_modules.memo.add(module_name)

            if module_name not in sys.modules:
                sys.path.insert(0, module_parent)
                importlib.import_module(module_name)
            elif str(module_pth) in sys.modules[module_name].__path__:
                logging.info(f"{module_pth} has already been imported.")
            else:
                raise ImportError(
                    "Failed to import {} because the corresponding module name "
                    "({}) is not globally unique. Please rename the directory to "
                    "something unique and try again.".format(module_pth, module_name)
                )

if __name__=="__main__":
    import_modules()
    print("called",import_modules.memo)
