function func(name = "default", age = 0) {
  console.log(`I'm ${name} , and ${age} old.`);
}

func();
func(undefined, 2);
func(null, 2);
func(undefined, undefined);
func("dan", null);
