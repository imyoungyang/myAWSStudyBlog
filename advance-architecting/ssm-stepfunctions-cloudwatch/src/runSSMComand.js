const aws = require('aws-sdk');
const ssm = new aws.SSM();

const runCommand = (documentName, instance) => new Promise(function(resolve, reject) {
  ssm.sendCommand({
    DocumentName: documentName,
    InstanceIds: [instance],
    TimeoutSeconds: 3600
  }, function(err, data) {
    if (err) {
      reject(JSON.stringify(err))
    }
    else {
      resolve(data)
    }
  })
  
});

/*
* @input {documentName, InstanceId}
* @return {CommandId: CommandId, InstanceId: InstanceId, Status: Status}
*/
exports.handler = async (event, context, callback) => {
  const result = await runCommand(event.documentName, event.InstanceId);
  const CommandId = result.Command.CommandId;
  const InstanceId = result.Command.InstanceIds[0];
  const Status = result.Command.Status;
  callback(null, {CommandId: CommandId, InstanceId: InstanceId, Status: Status, wait_time: 3});
};

