import os
import sys

litex_third_party_dir = os.path.join(os.path.dirname(__file__), "..", "third_party")

# retro-compat 2019-09-30
from litex.soc.interconnect import packet
sys.modules["litex.soc.interconnect.stream_packet"] = packet

# retro-compat 2019-09-29
from litex.soc.integration import export
sys.modules["litex.soc.integration.cpu_interface"] = export

from litex.tools.litex_client import RemoteClient
