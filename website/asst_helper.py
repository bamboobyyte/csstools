import openai
from time import sleep


def wait_for_run(
    client : openai.OpenAI, 
    run : openai.types.beta.threads.run.Run, 
    thread : openai.types.beta.thread.Thread) -> openai.types.beta.threads.run.Run:
    """
    Polls the OpenAI API to wait for a run to complete.
    
    Args:
    client (openai.OpenAI): The OpenAI client instance.
    run (openai.types.beta.threads.run.Run): The run object to monitor.
    thread (openai.types.beta.threads.Thread): The thread associated with the run.

    Returns:
    openai.types.beta.threads.run.Run: The updated run object after completion.
    """

    # Loop until the run status is neither 'queued' nor 'in progress'
    while run.status == "queued" or run.status == "in_progress":
        
        # Retrieve the latest status of the run
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        
        # Sleep for a short interval to limit rate of API calls
        sleep(0.5)
    return run


def get_response(
    client : openai.OpenAI, 
    asst_id : str, 
    user_msg : str) -> str:
    """
    Creates a thread, sends a message, and retrieves the response from the OpenAI assistant.
    
    Args:
    client (openai.OpenAI): The OpenAI client instance.
    asst_id (str): The assistant ID to use for generating the response.
    user_msg (str): The user message to send to the assistant.

    Returns:
    str: The assistant's response to the user message.
    """
    # Create a new thread
    thread = client.beta.threads.create()

    # Send the user's message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role='user',
        content=user_msg
    )

    # Creat the assistant's run in the thread
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=asst_id
    )

    # Wait for the run to complete
    wait_for_run(client, run, thread)

    # Retrieve messages following the user's message
    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
        order='asc',
        after=message.id
    )

    # Extract and return the text of the first assistant response
    response = [m.content[0].text.value for m in messages ]
    return response[0]