<script>
  import {fly} from 'svelte/transition';
  import ChatPrompt from './Prompt.svelte';
  let showWelcome = true;
  let showChatPrompt = false;
  function startChatPrompt() {
    showWelcome = false;
    setTimeout(() => {
      showChatPrompt = true;
    }, 400);
  }
  let isMainPageShown = true;
  function showMainPage(show) {
    isMainPageShown = show;
  }
</script>

{#if isMainPageShown}
{:else}
  <ChatPrompt showMainPage={showMainPage} />
{/if}

{#if showWelcome}
  <div class="welcome-container" transition:fly={{ y: -200, duration: 400, opacity: 0 }}>
    <div class="welcome-content">
      <h1>Welcome to Brontutor</h1>
      <p>Your personal AI-powered tutor.</p>
      <button on:click={startChatPrompt}>Get Started</button>
    </div>
  </div>
{:else if showChatPrompt}
  <ChatPrompt />
{/if}

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to right, #333333, #444444);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .welcome-container {
    text-align: center;
    color: white;
    max-width: 500px;
    margin: auto;
  }

  .welcome-content {
    background: rgba(255, 255, 255, 0.1);
    padding: 2rem;
    border-radius: 10px;
    backdrop-filter: blur(10px);
  }

  h1 {
    font-weight: 600;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }

  p {
    font-weight: 400;
    margin-bottom: 2rem;
  }

  button {
    padding: 10px 30px;
    border: none;
    background-color: #fff;
    color: #333333;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    outline: none;
  }

  button:hover {
    background-color: #bbdefb;
    transform: translateY(-3px);
  }

  button:active {
    transform: translateY(-1px);
  }
</style>
