import { useState } from 'react';
import { Streamdown } from 'streamdown';
import { connectToAgent } from '../lib/agent-client';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [streamedContent, setStreamedContent] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);
    setStreamedContent('');

    try {
      await connectToAgent(userMessage, (chunk) => {
        setStreamedContent((prev) => prev + chunk);
      });

      setMessages((prev) => [
        ...prev,
        { role: 'assistant', content: streamedContent },
      ]);
      setStreamedContent('');
    } catch (error) {
      console.error('Error communicating with agent:', error);
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', content: 'Error: Failed to connect to agent service.' },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full p-4">
      <div className="flex-1 overflow-y-auto mb-4 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`p-4 rounded-lg ${
              message.role === 'user'
                ? 'bg-blue-600 ml-auto max-w-[70%]'
                : 'bg-gray-800 mr-auto max-w-[70%]'
            }`}
          >
            {message.role === 'user' ? (
              <p>{message.content}</p>
            ) : (
              <Streamdown>{message.content}</Streamdown>
            )}
          </div>
        ))}
        {isLoading && streamedContent && (
          <div className="bg-gray-800 p-4 rounded-lg mr-auto max-w-[70%]">
            <Streamdown>{streamedContent}</Streamdown>
          </div>
        )}
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          disabled={isLoading}
          className="flex-1 bg-gray-800 border border-gray-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500 disabled:opacity-50"
          placeholder="Ask me anything..."
        />
        <button
          onClick={handleSend}
          disabled={isLoading}
          className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 px-6 py-2 rounded-lg font-semibold disabled:opacity-50"
        >
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
}
