exports.handler = (event, context, callback) => {
    const connectionId = event.requestContext.connectionId;
    console.log("disconnect: " + connectionId);
    callback(null, {
        statusCode: 200,
    });
};
