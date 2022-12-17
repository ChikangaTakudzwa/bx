#!/bin/bash

SECRET_KEY=$(doppler secrets get --store dev --environment Development SECRET_KEY)
export SECRET_KEY
export DOPPLER_ENV=1
