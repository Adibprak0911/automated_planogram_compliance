import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/inlab22/Documents/automated_planogram_compliance-1/simulations/my_drone_simulation/install/my_drone_simulation'
