void vuln_func()
{
  char buf1[0x40];
  unsigned long var_1 = 0xcafebabedeabbeef;

  print_stack(buf1);
  
  puts("[*] Please input data in 'buf1' ...");
  gets(buf1);
}