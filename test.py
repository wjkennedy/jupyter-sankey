all_nodes = website_vists.Source.values.tolist() + website_vists.Dest.values.tolist()

source_indices = [all_nodes.index(source) for source in website_vists.Source] ## Retrieve source nodes indexes as per all nodes list.
target_indices = [all_nodes.index(dest) for dest in website_vists.Dest] ## Retrieve destination nodes indexes as per all nodes list.

colors = pex.colors.qualitative.D3

node_colors_mappings = dict([(node,np.random.choice(colors)) for node in all_nodes])

node_colors = [node_colors_mappings[node] for node in all_nodes]
edge_colors = [node_colors_mappings[node] for node in website_vists.Source] ## Color links according to source nodes

fig = go.Figure(data=[
                    go.Sankey(
                        node = dict(
                                pad = 20,
                                thickness = 20,
                                line = dict(color = "black", width = 1.0),
                                label =  all_nodes,
                                color =  node_colors,
                               ),
                        link = dict(
                               source =  source_indices,
                               target =  target_indices,
                               value =  website_vists.Count,
                               color = edge_colors
                               )
                         )
                    ])

fig.update_layout(title_text="User Journey on Website",
                  height=600,
                  font=dict(size = 10, color = 'white'),
                  plot_bgcolor='black', paper_bgcolor='black')

fig.show()
