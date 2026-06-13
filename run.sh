#!/usr/bin/env bash

# ==============================================================================
# FPGA UDP Network Settings Summary:
# ------------------------------------------------------------------------------
# FPGA IP: 192.168.137.2          | Linux IP: 192.168.137.1/24
# FPGA Port: 6002                 | Linux Port: 6001
# Image: 1280x720 RGB888          | UDP Packet: 1312 Bytes (32 Header + 1280 Data)
#
# Recommended Tuning (for high-speed UDP):
# sudo sysctl -w net.core.rmem_max=134217728
# sudo sysctl -w net.core.rmem_default=134217728
# ==============================================================================

# Help / Usage
show_help() {
    echo "YOLO Upper Computer - Control Script"
    echo ""
    echo "Usage:"
    echo "  ./run.sh                     - Start the main GUI application"
    echo "  ./run.sh --setup <interface> - One-click network setup (IP & Buffers)"
    echo "  ./run.sh --help              - Show this help message"
    echo ""
    echo "Diagnostics (in tools/fpga/):"
    echo "  Probe: python3 tools/fpga/udp_linux_probe.py --port 6001"
    echo "  Sniff: sudo tcpdump -i <interface> -n 'udp port 6001'"
    echo ""
}

if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    show_help
    exit 0
fi

# Network Setup Routine
if [ "$1" == "--setup" ]; then
    IFACE=$2
    if [ -z "$IFACE" ]; then
        echo "Error: Interface name required."
        echo "Example: ./run.sh --setup enp3s0"
        echo ""
        ip -br addr
        exit 1
    fi
    echo "Configuring $IFACE for FPGA connection..."
    sudo ip addr flush dev "$IFACE"
    sudo ip addr add 192.168.137.1/24 dev "$IFACE"
    sudo ip link set "$IFACE" up
    sudo sysctl -w net.core.rmem_max=134217728
    sudo sysctl -w net.core.rmem_default=134217728
    echo "Network configuration applied successfully."
fi

# Main Application Execution
echo "------------------------------------------------"
echo "Starting YOLO Upper Computer..."
echo "Network Mode: FPGA UDP (Expects 192.168.137.1:6001)"
echo "Tip: Use './run.sh --help' for setup and tools."
echo "------------------------------------------------"

VENV=.venv
QT_LIB=$VENV/lib/python3.13/site-packages/PySide6/Qt/lib

# Ensure Qt libraries are found
export LD_LIBRARY_PATH=$QT_LIB:$LD_LIBRARY_PATH

cd src
uv run main.py
