if [ $1 == "thornode" ]
  then
    curl https://thornode.thorchain.info/thorchain/doc/swagger.json > thornode.json
  else
    curl https://midgard.thorchain.info/v2/swagger.json > midgard.json
fi
