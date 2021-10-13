async function main() {
    const YapeNFT = await ethers.getContractFactory("YapeNFT");
    
    // Start deployment, returning a promise that resolves to a contract object
    const yapeNFT = await YapeNFT.deploy();
    console.log("Contract deployed to address:", yapeNFT.address);
 }
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });