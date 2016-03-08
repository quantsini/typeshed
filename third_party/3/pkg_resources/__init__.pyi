# Stubs for pkg_resources (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# NOTE: Still a little bit incomplete.

from typing import (Any, List, Callable, Union, Tuple, Iterator, Iterable,
                    Dict, Optional, Pattern)
import io
from collections import namedtuple
import zipfile

from pkg_resources._vendor.packaging import version
from pkg_resources._vendor.packaging.specifiers import SpecifierSet


SetuptoolsVersionType = Union['SetuptoolsVersion', 'SetuptoolsLegacyVersion']
StrOrSequenceOfLines = Union[str, Iterable[str]]

PackageOrRequirementType = Union[str, 'Requirement']

# TODO
LoaderType = Any
ModuleType = Any
ProviderFactoryType = Callable[[ModuleType], 'IResourceProvider']

# entry point funcs types
EntryPointFuncsDist = Union['Distribution', 'Requirement', str]
EntryPointFuncsGroup = Dict[str, 'EntryPoint']
EntryPointFuncsMap = Dict[str, EntryPointFuncsGroup]

OnChangeCallback = Callable[['Distribution'], None]
InstallerCallback = Callable[['Requirement'], 'Distribution']
FindPluginsOutput = Tuple[List['Distribution'], Dict['Distribution', 'ResolutionError']]

ImporterClassType = Any
FinderCallable = Callable[[ImporterClassType, str, bool], Iterator['Distribution']]
ImporterType = Any
NamespaceHandlerCallable = Callable[[ImporterType, str, str, ModuleType], str]

EPAttrsType = Tuple[str, ...]
EPExtrasType = Tuple[str, ...]

require = ... # type: Optional[Callable[..., List[Distribution]]]
working_set = ... # type: Optional[WorkingSet]

class PEP440Warning(RuntimeWarning): ...

class _SetuptoolsVersionMixin:
    def __hash__(self) -> int: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...


class SetuptoolsVersion(_SetuptoolsVersionMixin, version.Version): ...
class SetuptoolsLegacyVersion(_SetuptoolsVersionMixin, version.LegacyVersion): ...


def parse_version(v: str) -> SetuptoolsVersionType: ...

class ResolutionError(Exception): ...

class VersionConflict(ResolutionError):
    @property
    def dist(self) -> Distribution: ...
    @property
    def req(self) -> Requirement: ...
    def report(self) -> str: ...
    # TODO: fill required_by
    def with_context(self, required_by) -> Union['VersionConflict', 'ContextualVersionConflict']: ...


class ContextualVersionConflict(VersionConflict):
    @property
    # TODO: fill required_by
    def required_by(self): ...

# TODO
class DistributionNotFound(ResolutionError):
    @property
    def req(self) -> Requirement: ...
    @property
    def requirers(self): ...
    @property
    def requirers_str(self) -> str: ...
    def report(self) -> str: ...

class UnknownExtra(ResolutionError): ...

EGG_DIST = ... # type: int
BINARY_DIST = ... # type: int
SOURCE_DIST = ... # type: int
CHECKOUT_DIST = ... # type: int
DEVELOP_DIST = ... # type: int

# TODO
def register_loader_type(loader_type: LoaderType,
                         provider_factory: ProviderFactoryType) -> None: ...
def get_provider(moduleOrReq: PackageOrRequirementType) -> Union['IResourceProvider', 'Distribution']: ...

get_platform = ... # type: Callable[[], str]

def compatible_platforms(provided: Optional[str], required: Optional[str]) -> bool: ...
def run_script(dist_spec, script_name: str) -> None: ...

run_main = ... # type: Any

def get_distribution(dist: EntryPointFuncsDist) -> 'Distribution': ...
def load_entry_point(dist: EntryPointFuncsDist, group: str, name: str) -> 'EntryPoint': ...
def get_entry_map(dist: EntryPointFuncsDist,
                  group: Optional[str] = None) -> EntryPointFuncsMap: ...
def get_entry_info(dist: EntryPointFuncsDist, group: str, name: str) -> Optional['EntryPoint']: ...

# TODO
class IMetadataProvider:
    def has_metadata(name): ...
    def get_metadata(name): ...
    def get_metadata_lines(name): ...
    def metadata_isdir(name): ...
    def metadata_listdir(name): ...
    def run_script(script_name, namespace): ...

# TODO
class IResourceProvider(IMetadataProvider):
    def get_resource_filename(manager, resource_name): ...
    def get_resource_stream(manager, resource_name): ...
    def get_resource_string(manager, resource_name): ...
    def has_resource(resource_name): ...
    def resource_isdir(resource_name): ...
    def resource_listdir(resource_name): ...

class WorkingSet:
    entries = ... # type: List[str]
    entry_keys = ... # type: Dict[str, List[str]]
    by_key = ... # type: Dict[str, Distribution]
    callbacks = ... # type: List[OnChangeCallback]

    def __init__(self, entries: List[str] = None) -> None: ...
    def add_entry(self, entry: str) -> None: ...
    def __contains__(self, dist: Distribution) -> bool: ...
    def find(self, req: Requirement) -> Distribution: ...
    def iter_entry_points(self, group: str,
                          name: str = None) -> Iterator[EntryPoint]: ...
    # TODO: add type RequirementsType and add here
    def run_script(self, requires, script_name: str) -> None: ...
    def __iter__(self) -> Iterator[Distribution]: ...
    def add(self, dist: Distribution,
            entry: str = None,
            insert: bool = ...,
            replace: bool = ...) -> None: ...
    def resolve(self, requirements: Iterable[Requirement],
                env: Environment = None,
                installer: Optional[InstallerCallback] = None,
                replace_conflicting: bool = ...) -> List[Distribution]: ...
    def find_plugins(self, plugin_env: Environment,
                     full_env: Optional[Environment] = None,
                     installer: Optional[InstallerCallback] = None,
                     fallback: bool = ...) -> FindPluginsOutput: ...
    # TODO: check requirements type
    def require(self, *requirements: StrOrSequenceOfLines) -> List[Distribution]: ...
    def subscribe(self, callback: OnChangeCallback) -> None: ...

class Environment:
    platform = ... # type: str
    python = ... # type: str
    def __init__(self, search_path: Iterable[str] = None,
                 platform: str = ...,
                 python: str = ...) -> None: ...
    def can_add(self, dist: Distribution) -> bool: ...
    def remove(self, dist: Distribution) -> None: ...
    def scan(self, search_path: Optional[Iterable[str]] = None) -> None: ...
    def __getitem__(self, project_name: str) -> List[Distribution]: ...
    def add(self, dist: Distribution) -> None: ...
    def best_match(self, req: Requirement,
                   working_set: WorkingSet,
                   installer: Optional[InstallerCallback] = None) -> Optional[Distribution]: ...
    def obtain(self, requirement: Requirement,
               installer: Optional[InstallerCallback] = None) -> Optional[Distribution]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __iadd__(self, other: Union[Distribution, 'Environment']) -> 'Environment': ...
    def __add__(self, other: Union[Distribution, 'Environment']) -> 'Environment': ...

AvailableDistributions = ... # type: Environment

class ExtractionError(RuntimeError): ...

class ResourceManager:
    extraction_path = ... # type: Any
    cached_files = ... # type: Any
    def __init__(self) -> None: ...
    def resource_exists(self, package_or_requirement: PackageOrRequirementType,
                        resource_name: str) -> bool: ...
    def resource_isdir(self, package_or_requirement: PackageOrRequirementType,
                       resource_name: str) -> bool: ...
    def resource_filename(self, package_or_requirement: PackageOrRequirementType,
                          resource_name: str) -> str: ...
    # TODO: return type
    def resource_stream(self, package_or_requirement: PackageOrRequirementType,
                        resource_name: str): ...
    # TODO: return type
    def resource_string(self, package_or_requirement: PackageOrRequirementType,
                        resource_name: str): ...
    def resource_listdir(self, package_or_requirement: PackageOrRequirementType,
                         resource_name: str) -> List[str]: ...
    def extraction_error(self) -> None: ...
    def get_cache_path(self, archive_name: str,
                       names: Iterable[str] = ...) -> str: ...
    def postprocess(self, tempname: str, filename: str) -> None: ...
    def set_extraction_path(self, path: str) -> None: ...
    def cleanup_resources(self, force: bool = ...) -> List[str]: ...

def get_default_cache() -> str: ...

def safe_name(name: str) -> str: ...

def safe_version(version: str) -> str: ...

def safe_extra(extra: str) -> str: ...

def to_filename(name: str) -> str: ...

def invalid_marker(text: str) -> Union[SyntaxError, bool]: ...

def evaluate_marker(text: str, extra=None) -> bool: ...


class NullProvider:
    egg_name = ... # type: Optional[str]
    egg_info = ... # type: Optional[str]
    loader = ... # type: Optional[LoaderType]
    module_path = ... # type: Optional[str]
    # TODO: init param
    def __init__(self, module) -> None: ...
    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> str: ...
    # TODO: return type
    def get_resource_stream(self, manager: ResourceManager, resource_name: str) -> io.BytesIO: ...
    # TODO: return type
    def get_resource_string(self, manager: ResourceManager, resource_name: str): ...
    def has_resource(self, resource_name: str) -> bool: ...
    def has_metadata(self, name: str) -> bool: ...
    def get_metadata(self, name: str) -> str: ...
    def get_metadata_lines(self, name: str) -> Iterator[str]: ...
    def resource_isdir(self, resource_name: str) -> bool: ...
    def metadata_isdir(self, name: str) -> bool: ...
    def resource_listdir(self, resource_name: str) -> List[str]: ...
    def metadata_listdir(self, name: str) -> List[str]: ...
    def run_script(self, script_name: str, namespace: Dict[str, Any]) -> None: ...


class EggProvider(NullProvider):
    # TODO: module type
    def __init__(self, module) -> None: ...


class DefaultProvider(EggProvider):
    # TODO: return type
    def get_resource_stream(self, manager: ResourceManager, resource_name: str): ...


class EmptyProvider(NullProvider):
    module_path = ... # type: Optional[str]
    def __init__(self) -> None: ...


empty_provider = ... # type: EmptyProvider


class ZipManifests(dict):
    @classmethod
    def build(cls, path): ...
    load = ... # type: Any


class MemoizedZipManifests(ZipManifests): ...


manifest_mod = namedtuple('manifest_mod', 'manifest mtime')
def load(self, path): ...


class ContextualZipFile(zipfile.ZipFile):
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...
    def __new__(cls, *args, **kwargs): ...


class ZipProvider(EggProvider):
    eagers = ... # type: Optional[List[str]]

    zip_pre = ... # type: str

    def __init__(self, module) -> None: ...

    @property
    def zipinfo(self): ...

    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> str: ...

class FileMetadata(EmptyProvider):
    path = ... # type: Any

    def __init__(self, path) -> None: ...

    def has_metadata(self, name: str) -> bool: ...
    # TODO
    def get_metadata(self, name: str): ...

    def get_metadata_lines(self, name): ...


class PathMetadata(DefaultProvider):
    module_path = ... # type: Optional[str]

    egg_info = ... # type: Optional[str]

    def __init__(self, path: str, egg_info: str) -> None: ...


class EggMetadata(ZipProvider):
    zip_pre = ... # type: str

    loader = ... # type: Optional[LoaderType]

    module_path = ... # type: Optional[str]

    def __init__(self, importer: ImporterType) -> None: ...

def register_finder(importer_type: ImporterClassType,
                    distribution_finder: FinderCallable): ...

def find_distributions(path_item: str,
                       only: bool = ...) -> Iterator['Distribution']: ...

def register_namespace_handler(importer_type: ImporterClassType,
                               namespace_handler: NamespaceHandlerCallable): ...

def declare_namespace(packageName: str) -> None: ...

# TODO:
def fixup_namespace_packages(path_item, parent=None): ...

def normalize_path(filename: str) -> str: ...

def yield_lines(strs: StrOrSequenceOfLines) -> Iterator[str]: ...

class EntryPoint:
    name = ... # type: str
    module_name = ... # type: str
    attrs = ... # type: EPAttrsType
    extras = ... # type: EPExtrasType
    dist = ... # type: Optional['Distribution']
    def __init__(self, name: str, module_name: str,
                 attrs: EPAttrsType=...,
                 extras: EPExtrasType=...,
                 dist: Optional['Distribution'] = None) -> None: ...
    def load(self,
             require: bool = ...,
             *args, **kwargs) -> Any: ...
    def resolve(self) -> Any: ...
    def require(self,
                env: Optional[Environment] = None,
                installer: Optional[InstallerCallback] = None) -> None: ...
    pattern = ... # type: Pattern
    @classmethod
    def parse(cls, src: str,
              dist: Optional['Distribution'] = None) -> 'EntryPoint': ...
    @classmethod
    def parse_group(cls, group: str, lines: StrOrSequenceOfLines,
                    dist: Optional['Distribution'] = None) -> EntryPointFuncsGroup: ...
    @classmethod
    def parse_map(cls,
                  data: Union[Dict[str, StrOrSequenceOfLines], StrOrSequenceOfLines],
                  dist: Optional['Distribution'] = None) -> EntryPointFuncsMap: ...

class Distribution:
    PKG_INFO = ... # type: str
    project_name = ... # type: str
    py_version = ... # type: str
    platform = ... # type: Optional[str]
    location = ... # type: str
    precedence = ... # type: int

    def __init__(self,
                 location: Optional[str] = None,
                 metadata: Optional[IResourceProvider] = None,
                 project_name: Optional[str] = None,
                 version: Optional[str] = None,
                 py_version: str = ...,
                 platform: Optional[str] = None,
                 precedence: int = ...) -> None: ...

    @classmethod
    def from_location(cls,
                      location: str,
                      basename: str,
                      metadata: Optional[IResourceProvider] = None,
                      **kw) -> 'Distribution': ...

    # TODO: add exact tuple form
    @property
    def hashcmp(self) -> Tuple[SetuptoolsVersionType, int, str, str, str, str]: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: 'Distribution') -> bool: ...
    def __le__(self, other: 'Distribution') -> bool: ...
    def __gt__(self, other: 'Distribution') -> bool: ...
    def __ge__(self, other: 'Distribution') -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

    @property
    def key(self) -> str: ...

    @property
    def parsed_version(self) -> SetuptoolsVersionType: ...

    @property
    def version(self) -> str: ...

    def requires(self,
                 extras: Iterable[str] = ...) -> List[Requirement]: ...

    def activate(self,
                 path: Optional[Iterable[str]] = None) -> None: ...

    def egg_name(self) -> str: ...

    def __getattr__(self, attr: str) -> Any: ...

    @classmethod
    def from_filename(cls, filename: str,
                      metadata: Optional[IResourceProvider] = None, **kw) -> 'Distribution': ...

    def as_requirement(self) -> Requirement: ...

    def load_entry_point(self, group: str, name: str) -> Any: ...

    def get_entry_map(self,
                      group: Optional[str] = None) -> EntryPointFuncsMap: ...

    def get_entry_info(self, group: str, name: str) -> Optional[EntryPoint]: ...

    def insert_on(self, path: List[str],
                  loc: Optional[str] = None,
                  replace: bool = ...) -> None: ...

    def check_version_conflict(self) -> None: ...

    def has_version(self) -> bool: ...

    def clone(self, **kw) -> 'Distribution': ...

    @property
    def extras(self) -> List[str]: ...


class EggInfoDistribution(Distribution): ...


class DistInfoDistribution(Distribution):
    PKG_INFO = ... # type: str
    EQEQ = ... # type: Pattern


class RequirementParseError(ValueError): ...


def parse_requirements(strs) -> Iterator['Requirement']: ...


class Requirement:
    project_name = ... # type: str
    key = ... # type: str
    specifier = ... # type: SpecifierSet
    specs = ... # type: List[Tuple[str, str]]
    extras = ... # type: Tuple[str]
    hashCmp = ... # type: Tuple[str, SpecifierSet, frozenset]

    def __init__(self, project_name: str, specs: List[Tuple[str, str]],
                 extras: Tuple[str]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __contains__(self, item: Union[Distribution, str]) -> bool: ...
    def __hash__(self) -> int: ...

    @staticmethod
    def parse(s: StrOrSequenceOfLines) -> 'Requirement': ...

def ensure_directory(path: str) -> None: ...

ContentType = List[str]
def split_sections(s) -> Iterator[Tuple[Optional[str], ContentType]]: ...

# Names in __all__ with no definition:
#   add_activation_listener
#   cleanup_resources
#   iter_entry_points
#   resource_exists
#   resource_filename
#   resource_isdir
#   resource_listdir
#   resource_stream
#   resource_string
#   set_extraction_path
