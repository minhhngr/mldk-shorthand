
# Introduction to Newman CLI

Newman is a command-line collection runner for Postman. It allows you to run and test Postman collections directly from the command line. 
This is particularly useful for automating API testing as part of your CI/CD pipeline.

## Installation

First, ensure you have Node.js and npm installed. Then, you can install Newman globally using npm:

```bash
npm install -g newman
```

## Basic Usage

### Running a Collection

To run a Postman collection with Newman, use the following command:

```bash
newman run <path-to-your-collection.json>
```

You can also run a collection directly from a URL or the Postman cloud:

```bash
newman run https://www.getpostman.com/collections/<collection-id>
```

### Running with an Environment

If your collection uses environment variables, you can specify an environment file:

```bash
newman run <path-to-your-collection.json> -e <path-to-your-environment.json>
```

## Advanced Usage

### Exporting Results

Newman allows you to export the results of your test runs in various formats, such as JSON, HTML, and JUnit:

```bash
newman run <path-to-your-collection.json> -r json,html,cli
```

### Iterations

You can run a collection multiple times using the `--iteration-count` flag:

```bash
newman run <path-to-your-collection.json> --iteration-count 10
```

You can also specify data files (in CSV or JSON format) to use different sets of data for each iteration:

```bash
newman run <path-to-your-collection.json> --iteration-data <path-to-your-data-file.json>
```

### Custom Scripts

Newman supports running pre-request and test scripts written in JavaScript. You can include these scripts in your Postman collection or environment files.

### Integrating with CI/CD

Newman can be integrated with various CI/CD tools like Jenkins, Travis CI, and GitHub Actions. Here’s an example Jenkins pipeline script:

```groovy
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'npm install -g newman'
            }
        }

        stage('Run Newman Tests') {
            steps {
                sh 'newman run <path-to-your-collection.json> -e <path-to-your-environment.json> -r cli,junit --reporter-junit-export results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'results.xml'
            }
        }
    }
}
```

## Best Practices

- **Organize Collections and Environments:** Keep your collections and environments well-organized and versioned.
- **Use Environment Variables:** Avoid hardcoding values; use environment variables for flexibility.
- **Modularize Tests:** Break down large collections into smaller, modular collections for easier maintenance and faster execution.
- **Continuous Integration:** Integrate Newman with your CI/CD pipeline to ensure automated and consistent testing.

By following these guidelines, you can leverage Newman to automate and streamline your API testing process effectively.
