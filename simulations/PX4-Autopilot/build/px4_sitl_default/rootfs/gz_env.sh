#!/usr/bin/env bash

export PX4_GZ_MODELS=/home/inlab22/Documents/automated_planogram_compliance-1/simulations/PX4-Autopilot/Tools/simulation/gz/models
export PX4_GZ_WORLDS=/home/inlab22/Documents/automated_planogram_compliance-1/simulations/PX4-Autopilot/Tools/simulation/gz/worlds

export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:$PX4_GZ_MODELS:$PX4_GZ_WORLDS
