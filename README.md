# End-to-end-Object-Detection-Project


## Project Workflows

- constants
- config_enity
- artifact_enity
- components
- pipeline
- app.py


## Project Configuration

```bash
install aws cli from the following link
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
```bash
# configure aws credentials (secret key and access key)
aws configure
```
```bash
# create a S3 bucket for model pusher, name is mentioned in the constant
```
## How to run?

```bash
conda create -p env python=3.8 -y
```
```bash
conda activate env/
```
```bash
pip install -r requirements.txt
```

```bash
python app.py 
```