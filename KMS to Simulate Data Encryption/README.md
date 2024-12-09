Link Labex : https://labex.io/courses/use-alibaba-cloud-kms-to-simulate-data-encryption

**Install AliyunCLI**
wget https://labex-ali-data.oss-us-west-1.aliyuncs.com/kms/aliyun-cli-linux-3.0.90-amd64.tgz
tar -zxvf aliyun-cli-linux-3.0.90-amd64.tgz
mv aliyun /usr/local/bin
aliyun --help

**Configure AliyunCli**
aliyun configure --profile akProfile

**Use Alibaba Cloud CLI to demonstrate the encryption and decryption functions of KMS**
aliyun kms ListKeys

Copy the key ID and enter the following command (replace YOUR-KEY-ID with your key ID) to show the key details:
aliyun kms DescribeKey --KeyId YOUR-KEY-ID
