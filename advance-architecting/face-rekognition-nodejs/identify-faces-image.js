const fs = require('fs');
const sharp = require('sharp');
var AWS = require('aws-sdk');
AWS.config.region = 'us-east-1';

var rekognition = new AWS.Rekognition();

var photo='group.jpg';
var collectionId='beyoung-demo';

const searchFacesByImage = (data) => {
    var args = {
        "CollectionId": collectionId,
        "FaceMatchThreshold": 70,
        "Image": { 
            "Bytes": data,
        },
        "MaxFaces": 1
    };
    rekognition.searchFacesByImage(args, function(err, resp) {
        if (err) {
            console.log(err);
            return;
        }
        if (resp.FaceMatches && resp.FaceMatches.length > 0 && resp.FaceMatches[0].Face)
        {
            console.log(resp.FaceMatches[0].Face);  
        } else {
            console.log("Not recognized");
        }
    });
};

const detectFaces = () => {
    var bitmap = fs.readFileSync(photo);
    var params = {
        "Image": { "Bytes": bitmap},
        "Attributes": ["DEFAULT"]
    };
    
    rekognition.detectFaces(params, function(err, data) {
      if (err) {
          console.log(err, err.stack);
          return;
      };
    
      if (data.FaceDetails && data.FaceDetails.length > 0) {
          var image = sharp(photo);
          image.metadata().then(function(metadata){
              var width = metadata.width;
              var height = metadata.height;
    
              data.FaceDetails.forEach((item, index) => {
                var boundingBox = item.BoundingBox;
                image
                    .extract({ left: Math.round(width * boundingBox.Left), 
                              top: Math.round(height * boundingBox.Top),
                              width: Math.round(width * boundingBox.Width),
                              height: Math.round(height * boundingBox.Height) })
                    .toBuffer().then( data => {
                        searchFacesByImage(data);
                        fs.writeFile(index + '.jpg', data, { flag: 'w' }, 
                        (err) => { if (err) console.log(err)});
                    });
              });
          });
      }
    });
};

detectFaces();
