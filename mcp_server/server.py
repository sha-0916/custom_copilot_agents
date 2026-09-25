from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sql-server")


@mcp.tool()
def ping():
    return {"status": "ok"}


if __name__ == "__main__":
    mcp.run()