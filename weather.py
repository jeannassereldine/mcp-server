from mcp.server.fastmcp import FastMCP
from tools import get_forcast
# Initialize FastMCP server
mcp = FastMCP("weather")


get_forcast.register(mcp)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')