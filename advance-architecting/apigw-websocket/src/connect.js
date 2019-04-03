exports.handler = (event, context, callback) => {
    const connectionId = event.requestContext.connectionId;
    console.log("connectionId: " + connectionId);
    const response = {
        statusCode: 200
    };
    callback(null, response);
};
