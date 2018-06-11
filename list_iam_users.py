import boto3

iam = boto3.client('iam')

def user_details():
    for user in iam.list_users()['Users']:
        print("UserName: " + user['UserName'])

        Groups = iam.list_groups_for_user(UserName=user['UserName'])
        for groupname in Groups['Groups']:
            print("GroupName: " + groupname['GroupName'])

        print("----------------------------")

user_details()
