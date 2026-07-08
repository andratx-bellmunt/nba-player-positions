"""Plotting utilities."""

from typing import List
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_features_boxplots(df: pd.DataFrame, features: List[str], target: str) -> None:
    """Plot a boxplot for each feature with respect to the target categories."""
    # Initialize a 3x4 subplot grid (here we are using that we know that len(features) == 12)
    fig = make_subplots(
        rows=4,
        cols=3,
        subplot_titles=features,  # Dynamic titles matching feature names
        vertical_spacing=0.08,    # Space out rows to keep text readable
        horizontal_spacing=0.06
    )

    # Iterate through features and map them to row/col indices
    for i, feature in enumerate(features):
        # Plotly grid indices are 1-based (not 0-based)
        row = (i // 3) + 1
        col = (i % 3) + 1

        # Add boxplot trace to specific grid coordinate
        fig.add_trace(
            go.Box(
                x=df[target],
                y=df[feature],
                name="",                    # Hides redundant individual names on x-axis
                boxpoints="outliers",       # Options: 'all', 'outliers', or False
                notched=False,
                marker_color="#1f77b4"    # Custom thematic styling choice
            ),
            row=row,
            col=col
        )

    # Optimize layout configuration for complex grid densities
    fig.update_layout(
        height=1200,
        width=800,
        title_text="Statistical Profiling: 12-Feature Boxplot Matrix",
        showlegend=False,           # Traces are self-evident
        template="plotly_dark"
    )

    # Render figure
    fig.show()


def plot_clusters_against_target(df: pd.DataFrame, positions: List[str]) -> None:
    """Stacked bar plot comparing actual positions with predicted clusters."""
    # Copy data
    dfc = df.copy()

    # Build and normalize the cross-tabulation matrix (Percentages per row)
    crosstab = pd.crosstab(dfc['POSITION'], dfc['CLUSTER'])
    crosstab_pct = crosstab.div(crosstab.sum(axis=1), axis=0) * 100

    # Reorder the rows to match our basketball layout sequence
    crosstab_pct = crosstab_pct.reindex(positions)

    # Initialize figure
    fig = go.Figure()

    # Define a distinct color palette for the 3 clusters
    cluster_colors = {0: '#1f77b4', 1: '#ff7f0e', 2: '#2ca02c'}

    # 4. Add each cluster as an independent stacked trace
    for cluster_id in [0, 1, 2]:
        # Pull percentages across positions for this specific cluster ID
        y_percentages = crosstab_pct[cluster_id].values

        fig.add_trace(
            go.Bar(
                x=positions,
                y=y_percentages,
                name=f"Cluster {cluster_id}",
                marker_color=cluster_colors.get(cluster_id, '#7f7f7f'),
                hovertemplate="<b>Position:</b> %{x}<br>" +
                              "<b>Proportion:</b> %{y:.1f}%<br>" +
                              "<extra></extra>"
            )
        )

    # 5. Enforce stacking and styling properties
    fig.update_layout(
        title={
            'text': "Playstyle Cluster Distributions Across Listed Positions",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Listed Position Profile",
        yaxis_title="Proportion of Position Category (%)",
        barmode='stack',
        template='plotly_dark',
        yaxis_ticksuffix='%',
        yaxis_range=[0, 100],
        legend_title_text="Assigned Cluster",
        height=500,
        width=800
    )

    fig.show()


def stylised_correlation_matrix(pds: pd.Series) -> pd.DataFrame:
    """Creates a stylised correlation matrix from a pandas series."""
    corr_matrix = (
        pds
        .corr()
        .style
        .background_gradient(cmap='coolwarm')
        .set_properties(width='50px')
        .format('{:.2f}')
        .set_table_styles([
            # Force column width and right-alignment on data cells (td)
            {'selector': 'td', 'props': [('width', '50px'), ('text-align', 'right'), ('padding', '5px')]},
            # Force column width and center-alignment on headers (th)
            {'selector': 'th', 'props': [('width', '50px'), ('text-align', 'center'), ('padding', '5px')]},
            # Optional: Prevent cell content from wrapping awkwardly
            {'selector': 'table', 'props': [('table-layout', 'fixed'), ('width', 'auto')]}
        ])
    )

    return corr_matrix
