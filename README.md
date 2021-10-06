# Zen-Money


## For embedding the chatbot

<script>
  window.watsonAssistantChatOptions = {
      integrationID: "46c9ef0c-a7ba-4b86-8c60-52f139613bbe", // The ID of this integration.
      region: "us-south", // The region your integration is hosted in.
      serviceInstanceID: "7efa1dc7-3d55-4169-ab6b-495ef9793cea", // The ID of your service instance.
      onLoad: function(instance) { instance.render(); }
    };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
      (window.watsonAssistantChatOptions.clientVersion || 'latest') +
      "/WatsonAssistantChatEntry.js"
    document.head.appendChild(t);
  });
</script>
