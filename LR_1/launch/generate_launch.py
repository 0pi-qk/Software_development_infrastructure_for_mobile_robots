import sys

def generate_start_launch(num_cycles):
	with open("start.launch", "w") as f:
		f.write("<launch>\n")
		f.write('    <node pkg="turtlesim" type="turtlesim_node" name="turtlesim_node" output="screen" />\n')
		f.write('    <node pkg="turtlesim" type="turtle_teleop_key" name="turtle_teleop_key" output="screen" />\n\n')

		for i in range(num_cycles):
			f.write('    <node pkg="turtle_stalker" type="turtle_stalker_node" name="turtle_stalker_node_{}" output="screen" args="1.0 turtle{} turtle{}" />\n'.format(i + 1, i + 2, i + 1))

		f.write("</launch>")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 generate_launch.py <num_cycles>")
		sys.exit(1)

	num_cycles = int(sys.argv[1])
	generate_start_launch(num_cycles)
