# import matplotlib.pyplot as plt
# import matplotlib.tri as tri
# import numpy as np

# def new_plot():
#     # First create the x and y coordinates of the points.
#     n_angles = 48
#     n_radii = 8
#     min_radius = 0.25
#     # radii = np.linspace(min_radius, 0.95, n_radii)
#     radii = [0.8, 0.5, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

#     angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=True)
#     angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
#     angles[:, 1::2] += np.pi / n_angles

#     x = (radii * np.cos(angles)).flatten()
#     y = (radii * np.sin(angles)).flatten()
#     z = (np.cos(radii) * np.cos(3 * angles)).flatten()

#     # Create the Triangulation; no triangles so Delaunay triangulation created.
#     triang = tri.Triangulation(x, y)

#     # Mask off unwanted triangles.
#     triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
#                             y[triang.triangles].mean(axis=1))
#                     < min_radius)
    
#     fig1, ax1 = plt.subplots()
#     ax1.set_aspect('equal')
#     tcf = ax1.tricontourf(triang, z)
#     fig1.colorbar(tcf)
#     ax1.tricontour(triang, z, colors='k')
#     # ax1.set_title('Contour plot of Delaunay triangulation')
#     plt.show()



# if __name__ == '__main__':
#     new_plot()