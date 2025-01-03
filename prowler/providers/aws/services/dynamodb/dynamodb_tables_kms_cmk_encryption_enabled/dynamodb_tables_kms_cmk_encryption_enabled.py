from prowler.lib.check.models import Check, Check_Report_AWS
from prowler.providers.aws.services.dynamodb.dynamodb_client import dynamodb_client


class dynamodb_tables_kms_cmk_encryption_enabled(Check):
    def execute(self):
        findings = []
        for table_arn, table in dynamodb_client.tables.items():
            report = Check_Report_AWS(self.metadata())
            report.resource_id = table.name
            report.resource_arn = table_arn
            report.resource_tags = table.tags
            report.region = table.region
            report.status = "FAIL"
            report.status_extended = (
                f"DynamoDB table {table.name} is using DEFAULT encryption."
            )
            if table.encryption_type == "KMS":
                report.status = "PASS"
                report.status_extended = f"DynamoDB table {table.name} has KMS encryption enabled with key {table.kms_arn.split('/')[1]}."
            findings.append(report)
        return findings
