**How to Build and Run the Docker Image:**

1.  **Save the Dockerfile:** Save the code above as `Dockerfile` in a directory.

2.  **Build the Docker image:**
    Open a terminal in the same directory as your `Dockerfile` and run the following command to build the image:

    ```bash
    docker build -t character-gen-nandy .
    ```
    *   `docker build`:  Command to build a Docker image.
    *   `-t character-gen-nandy`:  Tags the image with the name `character-gen-nandy`. You can choose a different name.
    *   `.`:  Specifies that the Dockerfile is in the current directory.

3.  **Run the Docker container:**
    To run the container and access a shell inside it, use the following command. **Crucially, pass your Google AI API key as an environment variable when running the container:**

    ```bash
    docker run -it --rm -e GEMINI_API_KEY="YOUR_ACTUAL_API_KEY" character-gen-nandy
    ```
    *   `docker run`: Command to run a Docker container.
    *   `-it`:  Runs the container in interactive mode and allocates a pseudo-TTY, giving you a shell inside the container.
    *   `--rm`:  Automatically removes the container when it exits (good for cleanups).
    *   `-e GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`:  **Sets the environment variable `GEMINI_API_KEY` inside the container**. **Replace `YOUR_ACTUAL_API_KEY` with your actual API key from Google AI Studio.**  This is the secure way to pass your API key.
    *   `character-gen-nandy`:  The name of the Docker image you built.
