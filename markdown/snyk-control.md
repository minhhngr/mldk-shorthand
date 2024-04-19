# SNYK

[DOCS]
- https://docs.snyk.io/
- https://docs.snyk.io/snyk-cli/commands/test

## Configuration

- npm install -g snyk
- snyk auth
- CLI
  - snyk test --all-projects --policy-path=.snyk --exclude=licenses
- Report
  - snyk test --json > snyk_report.json   (JSON Output)
  - snyk test --sarif > snyk_report.sarif (SARIF Output)
  - snyk test --json | snyk-to-html -o snyk_report.html (HTML Report)
    - Installation => npm install -g snyk-to-html (https://docs.snyk.io/snyk-cli/scan-and-maintain-projects-using-the-cli/cli-tools/snyk-to-html)
