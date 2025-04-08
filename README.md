<h1>  ReconX-AI</h1>

<p>
  <strong>ReconX-AI</strong> is an automated cybersecurity reconnaissance framework that combines 
  <em>traditional OSINT tools</em> with <em>AI-powered analysis</em> to assess targets more intelligently.
</p>

<p>
  This tool compares conventional recon techniques (like Nmap and WHOIS) with modern AI-enhanced parsing using 
  OpenAI's GPT models. It's designed for <strong>red teaming</strong>, <strong>automated OSINT</strong>, and 
  <strong>cybersecurity research</strong>.
</p>

<hr>

<h2>  Features</h2>
<ul>
  <li>⚙️ <strong>Traditional Recon:</strong> Gathers raw data using <code>Nmap</code> and <code>WHOIS</code>.</li>
  <li>  <strong>AI Parser:</strong> Feeds raw recon output to OpenAI GPT for intelligent parsing and categorization.</li>
  <li>  <strong>Comparison Engine:</strong> Automatically contrasts traditional vs AI-enhanced results.</li>
  <li>  <strong>Report Generator:</strong> Outputs a readable Markdown report in <code>output/report.md</code>.</li>
</ul>

<hr>

<h2>  Project Structure</h2>

<pre>
ReconX-AI/
├── .env                      # API key storage
├── main.py                  # Entry point for the app
├── data/                    # Stores Nmap & WHOIS raw output
├── output/                  # Final comparison report
└── modules/
    ├── traditional_recon.py     # Nmap + WHOIS script
    ├── ai_recon_parser.py       # AI parsing logic
    ├── comparator.py            # Compares recon outputs
    └── report_generator.py      # Creates Markdown reports
</pre>

<hr>

<h2>  Installation & Usage</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/yourusername/ReconX-AI.git
cd ReconX-AI
</code></pre>

<h3>2. Install Requirements</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Setup OpenAI API Key</h3>
<p>Create a <code>.env</code> file in the root directory:</p>
<pre><code>OPENAI_API_KEY=your-api-key</code></pre>

<p>
Get your API key from 
<a href="https://platform.openai.com/account/api-keys" target="_blank">platform.openai.com</a>.
</p>

<h3>4. Run the Application</h3>
<pre><code>python main.py</code></pre>

<hr>

<h2>  Output Example</h2>

<p>After running the tool, you’ll find a structured report here:</p>
<pre><code>output/report.md</code></pre>

<p>This includes:</p>
<ul>
  <li>  Traditional recon output</li>
  <li>  AI-enhanced analysis</li>
  <li>  Summary comparison</li>
</ul>

<hr>

<h2> Use Cases</h2>
<ul>
  <li>Red Team Automation</li>
  <li>AI-Enhanced OSINT</li>
  <li>Threat Intelligence</li>
  <li>Cybersecurity Research</li>
  <li>Master’s Thesis Projects</li>
</ul>

<hr>

<h2> Tech Stack & Dependencies</h2>
<ul>
  <li><code>openai</code></li>
  <li><code>python-dotenv</code></li>
  <li><code>nmap</code> (CLI)</li>
  <li><code>python-whois</code></li>
  <li><code>subprocess</code></li>
  <li><code>markdown2</code> (optional for HTML export)</li>
</ul>

<p>Install all with:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2> License</h2>
<p>MIT License © 2025 <strong> Prince Boadu</strong></p>

<hr>

<h2> Contributions</h2>
<p>
Pull requests are welcome! If you’d like to improve something or report a bug, feel free to 
<a href="https://github.com/yourusername/ReconX-AI/issues">open an issue</a>.
</p>


