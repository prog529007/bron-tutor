<script>
  let question = '';
  let prompts = [
    "Explain how to solve a linear system",
    "How can I find eigenvalues of a matrix",
    "Teach me how to multiply two matrices",
    "Explain the pythagorean theorem",
  ];

  function selectPrompt(prompt) {
    question = prompt;
  }
  export let showMainPage;
  function goBack() {
    showMainPage(true);
  }
</script>

{#if !showMainPage}
  <button class="back-button" on:click={goBack}>Back</button>
{/if}

<div class="prompt-container">
  <div class="prompt-suggestions">
    {#each prompts as prompt}
      <button class="prompt" on:click={() => selectPrompt(prompt)}>
        {prompt}
      </button>
    {/each}
  </div>
  <div class="input-group">
    <input type="text" bind:value={question} placeholder="Message Brontutor..." />
    <button>Submit</button>
  </div>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
    background: #121212; /* Dark background */
    color: #fff; 
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100vh;
  }

  .prompt-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    height: 100%;
    padding: 2rem;
  }

  .prompt-suggestions {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin-bottom: auto;
  }

  .prompt {
    background: none;
    border: 2px solid #555;
    border-radius: 16px; 
    padding: 10px 20px;
    font-size: 16px;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
  }

  .prompt:hover {
    background-color: #333;
    transform: scale(1.05);
  }

  .input-group {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 1rem;
    width: 80%;
    max-width: 600px; 
  }

  input {
    padding: 1.5rem;
    border: 2px solid #555;
    border-radius: 30px;
    font-size: 1rem;
    color: #121212;
    background: #fff;
    flex-grow: 1;
  }

  button {
    padding: 1.5rem 2rem; 
    border: none;
    background-color: #333;
    color: white;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s;
    font-size: 1rem; 
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
  }

  button:hover {
    background-color: #444444;
  }

  .back-button {
    position: fixed;
    top: 2rem;
    left: 2rem;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border: none;
    background-color: #444;
    color: white;
    border-radius: 22px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .back-button:hover {
    background-color: #333;
  }

</style>
