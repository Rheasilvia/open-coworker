import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <div className="h-screen w-screen bg-gray-900 text-white">
      <div className="flex flex-col h-full">
        <header className="bg-gray-800 p-4 border-b border-gray-700">
          <h1 className="text-2xl font-bold">Open-Coworker</h1>
          <p className="text-sm text-gray-400">AI-Powered Development Assistant</p>
        </header>
        <main className="flex-1 overflow-hidden">
          <ChatWindow />
        </main>
      </div>
    </div>
  );
}

export default App;
