
echo "Logging in to Doppler..."
doppler login -y

doppler -t $TKN setup


# doppler_project=$(doppler -t $TKN projects get brandxpert)
# echo "$doppler_project"
# doppler_config=$(doppler -t $TKN configs get dev)
# echo "$doppler_config"

# SECRET_KEY=$(doppler -t $TKN secrets get SECRET_KEY)
# export SECRET_KEY
