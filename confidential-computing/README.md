# mc2-playground

1. Launch an `Standard DC8s v3` VM on Azure.
2. Follow https://mc2-project.github.io/client-docs/install.html to install MC2 Docker image, and enter its shell.
3. Clone this repository
4. Download https://lsf-berkeley-edu.s3.amazonaws.com/amazon_full.csv.xz and unzip it to the `data` subdirectory.
5. Follow https://mc2-project.github.io/client-docs/quickstart.html to run the example. In Step 2, instead of `cp -r quickstart/* playground`, copy everything from this repository to playground instead.
    - If `mc2 upload` fails, just retry a few times.
6. Measure end-to-end runtime.
