const aws = require('aws-sdk');
const ssm = new aws.SSM();

const getStatus = (params) => new Promise(function(resolve, reject) {
  ssm.getCommandInvocation(params, function(err, data) {
    if (err) reject(err);
    else resolve(data); // successful response
  });  
});


/*
* @input {CommandId:, InstanceId:, Status}
*/
exports.handler = async(event, context, callback) => {
  const result = await getStatus({CommandId: event.CommandId, InstanceId: event.InstanceId, PluginName: "date"});
  console.log(result);
  const Status = result.Status;
  callback(null, {CommandId: event.CommandId, InstanceId: event.InstanceId, Status: Status});
};

