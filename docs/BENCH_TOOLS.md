<!--
=============================================================================
HYDRA-UMC-DOCS - Bench tools: a simulated tool head, the tool catalogue and the maturity ledger
Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
CC BY-SA 4.0 - see LICENSE.md
=============================================================================
-->

# Bench tools

Three small tools that let the ecosystem be tried and read without the board in hand. All of them are derived or simulated, and
none of them writes to a real device.

## The simulated tool head (`tools/fake_urtc.py`)

A URTC tool head that exists only as software. It answers two read-only queries on a CAN bus with the frames that the
cross-implementation vectors of URTC fix byte for byte:

| Request | Answer |
|---|---|
| `0x110` query the active tool | `0x111`, four to six bytes: tool, system error, CAN error, booting, and (when set) thermal fault and reset cause |
| `0x7F8` query the version | `0x7F9`, then `0x7FA` (only as the bootloader) and `0x7E9` (the patch, unless the head is set to predate it) |

Every other frame is ignored. It is a responder for the queries, not a simulation of motion, heating or flashing.

The state of the head is `data/fake_urtc.json` (tool, errors, reset cause, hardware id, version, patch, bootloader or application,
bootloader version); an unknown key or a value out of range is refused. `--tool N` overrides the tool.

On Linux, create the virtual interface (the tool prints these commands and never runs them), start the head, and point any CAN
client at the same interface:

```
python tools/fake_urtc.py --print-setup
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
python tools/fake_urtc.py --interface vcan0 --tool 5
```

**What is tested and what is not.** The responder is tested against the vectors of URTC (read from `URTC-DOCS` when it is next to
this repository, and written out in the tests otherwise) and against an in-memory bus. The SocketCAN bus is tested against a
simulated socket module: the layout of the 16-byte frame, the filtering of extended, remote and error frames, and the errors. It was
not run on a real Linux SocketCAN interface (`vcan` does not exist on Windows), so the first run on Linux is still to be done.

## The catalogue of tools (`data/urtc_tools.json`)

`tools/make_urtc_tools.py` reads the `ToolMode_t` enum of the URTC firmware and the headings of its tool document and writes the
twenty-five tools (number, constant name, title, and whether an expansion board is none, recommended or required), plus the number
that names no tool. `--check` fails when the file no longer matches those sources. The entries are the static part of the
`ToolDescriptor` contract of the SDK; the contract also requires a `kind`, a classification nobody has made, so
`urtc_tools.to_descriptors` refuses to build descriptors until it is given one for every tool.

`urtc_tools.resolve` turns what a client sends (a number, `0x05`, `TOOL_DRILL`, `drill`) into the one tool it means, or nothing.

**Pending, in other repositories:** the server still takes the tool as a free string; making it accept only what `resolve` accepts,
and publishing the catalogue as part of the SDK, are changes to the server and the SDK. The `kind` of each tool is an open decision.

## The maturity ledger (`data/maturity_ledger.json`)

`tools/make_ledger.py` writes, for every repository of the family, its maturity next to what it has been tried on (`none`,
`host-test`, `simulator`, `bench`, `hardware`), with a colour token per kind of evidence (`neutral`, `info`, `warn`, `ok_soft`,
`ok`), the hardware statement of the glance data, and the observations (`gaps`) that follow: a hardware-bound project that has not met
hardware, a project past scaffolding with no evidence recorded. The labels come in the eight languages. The file holds no date and no
version, so it changes only when a maturity, an evidence or a hardware statement does. `--check` fails when it is out of date.

The gaps are observations, not verdicts: nothing fails because of them.

**Pending, in another repository:** showing the ledger in the "ecosystem map" panel of the studio is a change to the studio; the file
is the contract it can read.
