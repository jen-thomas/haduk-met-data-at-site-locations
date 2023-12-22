#!/bin/bash -x

# The following code is taken from https://help.ceda.ac.uk/article/4442-ceda-opendap-scripted-interactions

mkdir -p ceda_data
cd ceda_data

git clone https://github.com/cedadev/online_ca_client
cd online_ca_client/contrail/security/onlineca/client/sh/

./onlineca-get-trustroots-wget.sh -U https://slcs.ceda.ac.uk/onlineca/trustroots/ -c trustroots -b

./onlineca-get-cert-wget.sh -U  https://slcs.ceda.ac.uk/onlineca/certificate/ -c trustroots -l "$CEDA_USERNAME" -o $PWD/creds.pem

curl --cert $PWD/creds.pem -L -c /dev/null http://dap.ceda.ac.uk/thredds/fileServer/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/1km/tas/ann/v20181126/tas_hadukgrid_uk_1km_ann_188901-188912.nc -o tas_hadukgrid_uk_1km_ann_188901-188912.nc