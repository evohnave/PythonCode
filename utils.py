from multiprocessing import cpu_count
from pkgutil import iter_modules

def module_exists(module_name: str) -> bool:
  ''' Determines if module_name is installed '''
  return module_name in (name for loader, name, ispkg in iter_modules())

def how_many_cores() -> int:
  ''' Determines how many cores '''
  return cpu_count()

#
