

# 🌦️ MCP Weather Server

A simple and modular **MCP (Modular Command Protocol) server** that exposes weather-related tools — perfect for integration with AI agents, LLMs, or any tool-using client.

This project demonstrates how to create and serve tools such as:

* `get_coordinates(city)`
* `get_forecast(latitude, longitude)`

Designed to be lightweight, clean, and easy to extend.

---

## 🧠 What Is MCP?

**MCP (Modular Command Protocol)** is a protocol for exposing tools (Python functions) in a machine-readable format so they can be:

* Automatically discovered
* Dynamically called by AI agents
* Interoperable across systems

It’s built for **tool-using LLMs**, **agents**, and **next-gen integrations**.

---

## 📁 Project Structure

```
mcp-server/
├── main.py           # Starts the FastMCP server
├── tools   
|------ get_forcast.py         # MCP tools: get_coordinates and get_forecast
├── pyproject.toml   # Python dependencies
└── README.md         # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/jeannassereldine/mcp-server.git
cd mcp-server
```



### 3. Run the Server

```bash
uv run weather.py
```

This starts the MCP server over `stdio`. You can connect any MCP client that supports the protocol.

---

## 🔧 Tools Overview

### `get_coordinates(city: str) -> Tuple[float, float]`

Returns hardcoded latitude and longitude for a given city.

> ✅ Replace this with a real geolocation API like OpenCage or Google Maps.

---

### `get_forecast(latitude: float, longitude: float) -> str`

Returns a formatted weather forecast string for the given coordinates.

> ✅ Replace with a live weather API like [api.weather.gov](https://api.weather.gov).

---

### `format_forecast(forecasts: List[Dict]) -> str`

Helper function that formats multiple forecast entries into a readable string.

---

## 🧩 Want to Build an MCP Client?

Stay tuned! The next part of this project will include a lightweight client that can:

* Auto-discover tools
* Call them based on context
* Build real-time agent workflows

---

## 🧠 Use Cases

* Build agent backends with clean, callable tools
* Expose local or cloud-based APIs to LLMs
* Prototype tools for LangChain or OpenAI function-calling agents
* Teach MCP integration through a practical example

---

## 📌 License

This project is open-source under the **MIT License**.

---

## 👋 Contributing

Pull requests are welcome! Feel free to open issues or suggest features you'd like to see.

---

## 🔗 Related

* 📄 [Original article on LinkedIn](#) ← *(https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7349014151165313025)*




