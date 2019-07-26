import com.amazonaws.services.securitytoken.AWSSecurityTokenServiceClientBuilder
import com.amazonaws.services.securitytoken.model.GetCallerIdentityRequest

val accountId = AWSSecurityTokenServiceClientBuilder.standard().build()
    .getCallerIdentity(new GetCallerIdentityRequest()).getAccount()

val roleName = "SageMakerEMR"

val roleArn = s"arn:aws:iam::$accountId:role/$roleName"
