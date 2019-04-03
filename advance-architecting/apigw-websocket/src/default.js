const AWS = require('aws-sdk');
// Add ApiGatewayManagementApi to the AWS namespace
require('aws-sdk/clients/apigatewaymanagementapi');

exports.handler = async (event) => {

  const apigwManagementApi = new AWS.ApiGatewayManagementApi({
    apiVersion: '2018-11-29',
    endpoint: event.requestContext.domainName + '/' + event.requestContext.stage
  });
  
  const connectionId = event.requestContext.connectionId;
  const postData = 'try {"action": "echo", "data": "moew"}';
  
  const send = async (connectionId, postData) => {
    await apigwManagementApi.postToConnection({ ConnectionId: connectionId, Data: postData }).promise();
  };

  try {
    await send(connectionId, postData);
  } catch (e) {
    return { statusCode: 500, body: e.stack };
  }
  
  // console.log(event);
  return { statusCode: 200};
};
