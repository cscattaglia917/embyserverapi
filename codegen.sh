docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
-i /local/openapi-4.7.6.0.json \
-l python \
-o /local/out/python \
-c /local/config.json
