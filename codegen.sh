docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
-i /local/openapi-remote.json \
-l python \
-o /local/out/python \
-c /local/config.json
