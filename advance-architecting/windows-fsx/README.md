# Windows FSx

When creating your Amazon FSx file system, you join your file system to a directory **managed by AWS Directory Service** for Microsoft Active Directory. FSx file systems automatically verify the credentials of users that access file system data to enforce Windows access control lists (ACLs). 

To use a self-managed directory with FSx, establish **a one-way trust relationship** between that self-managed directory and an AWS-managed directory that you create.

Every Amazon FSx file system comes with a default Windows file share called **share**. The Windows ACLs for this shared folder are configured to **allow read/write access to domain users** and allow full control to the AWS Delegated FSx Administrators group in your Active Directory. To change the ACLs, you can map the share as a user that is a member of the AWS Delegated FSx Administrators group.


