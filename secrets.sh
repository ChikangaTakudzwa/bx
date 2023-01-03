#!/bin/bash

SECRET_KEY=$(doppler secrets get --environment Development SECRET_KEY)
config=$(doppler projects get)
export SECRET_KEY
