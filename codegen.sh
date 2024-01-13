docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3:3.0.46 generate \
-i /local/openapi_v3.json \
-l python \
-o /local/out/python \
-c /local/config.json
