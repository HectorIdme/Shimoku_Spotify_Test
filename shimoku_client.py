import os
from dotenv import load_dotenv
import shimoku_api_python as Shimoku

load_dotenv()

access_token = os.getenv('SHIMOKU_TOKEN')
universe_id: str = os.getenv('UNIVERSE_ID')
workspace_id: str = os.getenv('WORKSPACE_ID')

client = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
    verbosity='INFO',
)

client.set_workspace(uuid=workspace_id)
client.set_board('Spotify Songs 2023 Dashboard')


#client.menu_paths.delete_menu_path(name="Top Features")

