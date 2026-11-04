import torch
import torch.nn as nn

def get_checkpoint_path():
    """Return the path to save the best performing model checkpoint.
    
    Returns:
        checkpoint_path (str)
            The path to save the best performing model checkpoint
    """
    return 'best_model_checkpoint.pth'

class LinearRegression(nn.Module):
    def __init__(self, input_dim=1, output_dim=1):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

def create_loss_and_optimizer(model):
    """Create and return a loss function and optimizer.
    
    Parameters:
        model (torch.nn.Module)
            A neural network
    
    Returns:
        loss_fn (function)
            The loss function for the model
        optimizer (torch.optim.Optimizer)
            The optimizer for the model
    """
    return nn.MSELoss(), torch.optim.Adam(model.parameters(), lr=0.01)

def train(x, y, model, loss_fn, optimizer, checkpoint_path, num_epochs=1000):
    """Train a model.
    
    Parameters:
        x (torch.Tensor)
            The input data
        y (torch.Tensor)
            The expected output data
        model (torch.nn.Module)
            A neural network
        loss_fn (function)
            The loss function
        optimizer (torch.optim.Optimizer)
            The optimizer for the model
        checkpoint_path (str)
            The path to save the best performing checkpoint
        num_epochs (int)
            The number of epochs to train for
    
    Side Effects:
        - Save the best performing model checkpoint to `checkpoint_path`
    """
    best_loss = float('inf')
    model.train()
    for _ in range(num_epochs):
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        # Save exactly the parameters evaluated by this loss.
        if loss.item() < best_loss:
            best_loss = loss.item()
            torch.save(model.state_dict(), checkpoint_path)
        loss.backward()
        optimizer.step()
    # Include the final update in checkpoint selection.
    with torch.no_grad():
        loss = loss_fn(model(x), y)
        if loss.item() < best_loss:
            torch.save(model.state_dict(), checkpoint_path)

def load_model_checkpoint(checkpoint_path):
    """Load a model checkpoint from disk.

    Parameters:
        checkpoint_path (str)
            The path to load the checkpoint from
    
    Returns:
        model (torch.nn.Module)
            The model loaded from the checkpoint
    """
    state = torch.load(checkpoint_path, map_location='cpu', weights_only=True)
    output_dim, input_dim = state['linear.weight'].shape
    model = LinearRegression(input_dim, output_dim)
    model.load_state_dict(state)
    model.eval()
    return model
    
