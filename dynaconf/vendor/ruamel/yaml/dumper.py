from __future__ import absolute_import
_A=None
from .emitter import Emitter
from .serializer import Serializer
from .representer import Representer,SafeRepresenter,BaseRepresenter,RoundTripRepresenter
from .resolver import Resolver,BaseResolver,VersionedResolver
if False:from typing import Any,Dict,List,Union,Optional;from .compat import StreamType,VersionType
__all__=['BaseDumper','SafeDumper','Dumper','RoundTripDumper']
class BaseDumper(Emitter,Serializer,BaseRepresenter,BaseResolver):
	def __init__(A,stream,default_style=_A,default_flow_style=_A,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,block_seq_indent=_A,top_level_colon_align=_A,prefix_colon=_A):Emitter.__init__(A,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,block_seq_indent=block_seq_indent,dumper=A);Serializer.__init__(A,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags,dumper=A);BaseRepresenter.__init__(A,default_style=default_style,default_flow_style=default_flow_style,dumper=A);BaseResolver.__init__(A,loadumper=A)
class SafeDumper(Emitter,Serializer,SafeRepresenter,Resolver):
	def __init__(A,stream,default_style=_A,default_flow_style=_A,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,block_seq_indent=_A,top_level_colon_align=_A,prefix_colon=_A):Emitter.__init__(A,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,block_seq_indent=block_seq_indent,dumper=A);Serializer.__init__(A,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags,dumper=A);SafeRepresenter.__init__(A,default_style=default_style,default_flow_style=default_flow_style,dumper=A);Resolver.__init__(A,loadumper=A)
class Dumper(Emitter,Serializer,Representer,Resolver):
	def __init__(A,stream,default_style=_A,default_flow_style=_A,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,block_seq_indent=_A,top_level_colon_align=_A,prefix_colon=_A):Emitter.__init__(A,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,block_seq_indent=block_seq_indent,dumper=A);Serializer.__init__(A,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags,dumper=A);Representer.__init__(A,default_style=default_style,default_flow_style=default_flow_style,dumper=A);Resolver.__init__(A,loadumper=A)
class RoundTripDumper(Emitter,Serializer,RoundTripRepresenter,VersionedResolver):
	def __init__(A,stream,default_style=_A,default_flow_style=_A,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,block_seq_indent=_A,top_level_colon_align=_A,prefix_colon=_A):Emitter.__init__(A,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,block_seq_indent=block_seq_indent,top_level_colon_align=top_level_colon_align,prefix_colon=prefix_colon,dumper=A);Serializer.__init__(A,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags,dumper=A);RoundTripRepresenter.__init__(A,default_style=default_style,default_flow_style=default_flow_style,dumper=A);VersionedResolver.__init__(A,loader=A)