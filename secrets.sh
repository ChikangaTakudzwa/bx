#!/bin/bash

SECRET_KEY=$(doppler secrets get --environment Development SECRET_KEY)
export SECRET_KEY
